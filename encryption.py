import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def generarClave():
	return secrets.token_bytes(32)

def encriptar(mensaje, clave):
	backend = default_backend()
	cifrador = Cipher(algorithms.AES(clave), modes.CBC(b'\x00' * 16), backend=backend)
	cifrar = cifrador.encryptor()

	padder = padding.PKCS7(128).padder()

	msgPadding = padder.update(mensaje) + padder.finalize()
	mensajeEncriptado = cifrar.update(msgPadding) + cifrar.finalize()

	return mensajeEncriptado

def desencriptar(mensajeEncriptado, clave):
	backend = default_backend()
	cifrador = Cipher(algorithms.AES(clave), modes.CBC(b'\x00' * 16), backend=backend)
	descifrar = cifrador.decryptor()
	msgPadding = descifrar.update(mensajeEncriptado) + descifrar.finalize()
	unpadder = padding.PKCS7(128).unpadder()
	mensajeDesencriptado = unpadder.update(msgPadding) + unpadder.finalize()

	return mensajeDesencriptado