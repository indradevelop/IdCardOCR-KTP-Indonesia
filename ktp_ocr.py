from google import genai
from pydantic import BaseModel
from io import BytesIO
from PIL import Image

GOOGLE_API_KEY="your_google_api_key_here"
model_name = "gemini-2.5-flash-preview-05-20"

class IdCard(BaseModel):
    provinsi: str
    kota: str
    NIK: str
    nama: str
    tempat_tgl_lahir: str
    jenis_kelamin: str
    gol_darah: str
    alamat: str
    rt_rw: str
    kel_desa: str
    kecamatan: str
    agama: str
    status_perkawinan: str
    pekerjaan: str
    kewarganegaraan: str
    berlaku_hingga: str

prompt = "ID Card recognizer as a JSON object"
image = "image.jpg"
client = genai.Client(api_key=GOOGLE_API_KEY)
im = Image.open(BytesIO(open(image, "rb").read()))
im.thumbnail([1024,1024], Image.Resampling.LANCZOS)
response = client.models.generate_content(
    model=model_name,
    contents=[prompt, im],
    config={
        "response_mime_type": "application/json",
        "response_schema": IdCard,
    },
)


print(response.text)