# JobProfile

Encoding profile ID. Coffee-themed naming: prep time maps to encode speed, bare name is the 8-bit default (universal decoder compatibility), `-10bit` suffix opts into HEVC Main10 for higher-quality playback on newer decoders.  **8-bit (default):** - `sophon-espresso` — fastest, lowest compression - `sophon-cortado` — balanced speed and quality - `sophon-americano` — slowest, highest compression  **10-bit (HEVC Main10):** - `sophon-espresso-10bit` - `sophon-cortado-10bit` - `sophon-americano-10bit`  **Adaptive dispatcher:** - `sophon-auto` — public opt-in profile. The worker classifies   the source and records the concrete `effective_profile_id` on   the job once dispatch resolves. 

## Enum

* `SOPHON_MINUS_ESPRESSO` (value: `'sophon-espresso'`)

* `SOPHON_MINUS_CORTADO` (value: `'sophon-cortado'`)

* `SOPHON_MINUS_AMERICANO` (value: `'sophon-americano'`)

* `SOPHON_MINUS_ESPRESSO_MINUS_10BIT` (value: `'sophon-espresso-10bit'`)

* `SOPHON_MINUS_CORTADO_MINUS_10BIT` (value: `'sophon-cortado-10bit'`)

* `SOPHON_MINUS_AMERICANO_MINUS_10BIT` (value: `'sophon-americano-10bit'`)

* `SOPHON_MINUS_AUTO` (value: `'sophon-auto'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


