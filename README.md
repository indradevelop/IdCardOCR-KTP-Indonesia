# ID Card OCR for KTP Indonesia using Gemini AI

This project provides an Optical Character Recognition (OCR) solution to extract data from Indonesian KTP (ID Card) using Gemini AI.

## Setup Instructions

1. Create a virtual environment named `.venv`:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the environment variable `GOOGLE_API_KEY` in `ktp_ocr.py` with your Google Cloud API key

## Running the Sample Code

Run the sample code to perform OCR on KTP images:

```bash
python ktp_ocr.py
```

## Example Result

```json
{
  "provinsi": "JAWA TIMUR",
  "kota": "KEDIRI",
  "NIK": "3506042602660001",
  "nama": "SULISTYONO",
  "tempat_tgl_lahir": "KEDIRI, 26-02-1966",
  "jenis_kelamin": "LAKI-LAKI",
  "gol_darah": "-",
  "alamat": "JL.RAYA - DSN PURWOKERTO",
  "rt_rw": "002 / 003",
  "kel_desa": "PURWOKERTO",
  "kecamatan": "NGADILUWIH",
  "agama": "ISLAM",
  "status_perkawinan": "KAWIN",
  "pekerjaan": "GURU",
  "kewarganegaraan": "WNI",
  "berlaku_hingga": "26-02-2017"
}
```

Enjoy extracting data from Indonesian ID Cards with ease!