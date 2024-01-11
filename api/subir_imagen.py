from appwriteClient import storage
from appwrite.input_file import InputFile
import uuid

async def subir_imagen(file):
    id = str(uuid.uuid4())
    try:
        image_content = await file.read()
        storage.create_file('ads',id,InputFile.from_path(image_content))
        return {"message":f"La imagen fue subida exitosamente","id":id}
    except Exception as e:
        return e.message
