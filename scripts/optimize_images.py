"""Generate high-quality WebP copies of the site's photos; preserve all originals.

Run with Python and Pillow installed: python scripts/optimize_images.py
The JSON output lists responsive candidates and the default-download savings.
"""

import json
import re
from math import gcd
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PAGES = ("home.html", "about.html", "courses.html", "group-training.html")


def main():
    sources = set()
    for page in PAGES:
        markup = (ROOT / page).read_text(encoding="utf-8")
        for src in re.findall(r'\bsrc="(img/[^\"]+\.(?:png|webp))"', markup):
            sources.add(str(Path(src).with_suffix(".png")).replace("\\", "/"))

    report = []
    for source in sorted(sources):
        source_path = ROOT / source
        with Image.open(source_path) as original:
            original.load()
            # Keep the embedded color profile, alpha, and full photographic frame.
            # No cropping, sharpening, or color adjustments are applied.
            profile = original.info.get("icc_profile")
            photo = original.convert("RGBA" if "A" in original.getbands() else "RGB")
            if photo.mode == "RGBA" and photo.getchannel("A").getextrema() == (255, 255):
                photo = photo.convert("RGB")
            width, height = photo.size
            is_logo = source_path.stem == "aed_arizona_logo"
            max_edge = 2880 if "hero" in source_path.stem else 2400
            # Use integer multiples of the native ratio where possible.
            divisor = gcd(width, height)
            unit_w, unit_h = width // divisor, height // divisor
            scale = min(1, max_edge / max(width, height))
            if divisor > 1:
                multiple = max(1, int(divisor * scale))
                largest = (unit_w * multiple, unit_h * multiple)
            else:
                largest = (round(width * scale), round(height * scale))
            if is_logo:
                largest = photo.size

            dimensions = {largest}
            if not is_logo:
                for candidate_width in (640, 1280):
                    if candidate_width < largest[0] * 0.85:
                        if divisor > 1 and unit_w <= 64:
                            multiple = max(1, round(candidate_width / unit_w))
                            dimensions.add((unit_w * multiple, unit_h * multiple))
                        else:
                            dimensions.add((candidate_width, round(candidate_width * height / width)))

            candidates = []
            for target_size in sorted(dimensions):
                name = source_path.stem
                if target_size != largest:
                    name += f"-{target_size[0]}w"
                target = source_path.with_name(name + ".webp")
                resized = photo if photo.size == target_size else photo.resize(target_size, Image.Resampling.LANCZOS)
                options = {"format": "WEBP", "quality": 90, "method": 6, "lossless": is_logo}
                if profile:
                    options["icc_profile"] = profile
                resized.save(target, **options)
                candidates.append({"src": target.relative_to(ROOT).as_posix(), "width": target_size[0],
                                   "height": target_size[1], "bytes": target.stat().st_size})
            report.append({"original": source, "width": width, "height": height,
                           "original_bytes": source_path.stat().st_size, "candidates": candidates})
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
