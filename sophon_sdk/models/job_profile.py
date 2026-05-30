# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class JobProfile(str, Enum):
    """
    Encoding profile ID. Coffee-themed naming: prep time maps to encode speed (espresso = fast, cortado = medium, americano = slow). The naming suffixes compose:  - bare name → 8-bit HEVC Main (universal decoder compatibility,   default) - `-10bit` suffix → HEVC Main10 output. Requires a decoder that   supports Main10 (modern phones, modern TVs, Safari, Chrome   with hardware decode). Older / low-end devices may not play   Main10 output. Pick only when you know the downstream   pipeline supports it. - `-hq` suffix → quality-biased 8-bit variant for heavy source   formats (ProRes, DNxHD, high-bitrate camera originals,   mastering-grade intermediates). Files will be larger than   the standard tier; pick when preserving detail matters more   than bitrate. Broad device compatibility (8-bit Main). - `-hq-10bit` suffix → combines HQ with Main10 to preserve   10-bit depth end-to-end. Same Main10 compatibility caveat   as above; pick for ProRes 422/4444, DNxHD, BRAW, or camera   masters where detail AND bit depth matter and you control   the downstream pipeline.  **For broad audience playback, pick `sophon-auto` or an explicit 8-bit coffee profile.** `sophon-auto` produces 8-bit Main output regardless of source bit depth.  If you're not sure which to pick, use `sophon-auto` — the API picks per-source settings tuned for consistent output regardless of what you submit, and automatically re-encodes at stricter settings if the first pass doesn't hold up.  **8-bit (standard, default):** - `sophon-espresso` — fastest, lowest compression - `sophon-cortado` — balanced speed and quality - `sophon-americano` — slowest, highest compression  **8-bit HQ** (max quality preservation for heavy formats): - `sophon-espresso-hq` - `sophon-cortado-hq` - `sophon-americano-hq`  **10-bit (HEVC Main10):** - `sophon-espresso-10bit` - `sophon-cortado-10bit` - `sophon-americano-10bit`  **10-bit HQ** (max quality preservation AND preserves 10-bit depth): - `sophon-espresso-hq-10bit` - `sophon-cortado-hq-10bit` - `sophon-americano-hq-10bit`  **Adaptive dispatcher:** - `sophon-auto` — content-adaptive. The API probes each source,   picks tuned settings, and re-encodes at stricter settings if   the first pass doesn't hold up. `profile` on the job response   stays `sophon-auto`; `effective_profile_id` records the   concrete variant the API actually ran. 
    """

    """
    allowed enum values
    """
    SOPHON_MINUS_ESPRESSO = 'sophon-espresso'
    SOPHON_MINUS_CORTADO = 'sophon-cortado'
    SOPHON_MINUS_AMERICANO = 'sophon-americano'
    SOPHON_MINUS_ESPRESSO_MINUS_HQ = 'sophon-espresso-hq'
    SOPHON_MINUS_CORTADO_MINUS_HQ = 'sophon-cortado-hq'
    SOPHON_MINUS_AMERICANO_MINUS_HQ = 'sophon-americano-hq'
    SOPHON_MINUS_ESPRESSO_MINUS_10BIT = 'sophon-espresso-10bit'
    SOPHON_MINUS_CORTADO_MINUS_10BIT = 'sophon-cortado-10bit'
    SOPHON_MINUS_AMERICANO_MINUS_10BIT = 'sophon-americano-10bit'
    SOPHON_MINUS_ESPRESSO_MINUS_HQ_MINUS_10BIT = 'sophon-espresso-hq-10bit'
    SOPHON_MINUS_CORTADO_MINUS_HQ_MINUS_10BIT = 'sophon-cortado-hq-10bit'
    SOPHON_MINUS_AMERICANO_MINUS_HQ_MINUS_10BIT = 'sophon-americano-hq-10bit'
    SOPHON_MINUS_AUTO = 'sophon-auto'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobProfile from a JSON string"""
        return cls(json.loads(json_str))


