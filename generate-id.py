import io
import uuid


file = io.open('device.py', 'w')
file.write(f"ID = '{uuid.uuid4()}'")
file.close()
