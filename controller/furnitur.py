from services import furnitur as furniturService
from executeQuery import execute_query
from connectDB import conn

from services import warna as warnaService
from services import material as materialService

def getAllFurnitur():
    furnitur = execute_query(furniturService.getAllFurnitur)
    return furnitur

def getDetailFurnitur(id_furnitur, id_bagian_furnitur=None,  id_warna=None, id_material=None):
    detailFurniturList = execute_query(furniturService.getDetailFurniturById, id_furnitur, id_bagian_furnitur=id_bagian_furnitur, id_warna=id_warna, id_material=id_material)
    
    return detailFurniturList


def updateBagianFurnitur(id_bagian_furnitur, id_warna, id_material, nama_bagian_furnitur, panjang, lebar, tinggi, harga, stok):
    execute_query(furniturService.updateBagianFurnitur,id_bagian_furnitur, id_warna, id_material, nama_bagian_furnitur, panjang, lebar, tinggi, harga, stok)

    
def updateFurniture(id_furnitur, nama, deskripsi):
    execute_query(furniturService.updateFurnitur, id_furnitur, nama=nama, deskripsi=deskripsi)
    
def deleteFurnitur(id_furnitur, cursor=None):
    execute_query(furniturService.deleteFurnitur, id_furnitur)

def deleteBagianFurnitur(id_bagian_furnitur, cursor=None):
    execute_query(furniturService.deleteBagianFurnitur, id_bagian_furnitur)

def insertBagianFurnitur(idFurnitur, dataBagianFurnitur):
    cursor = conn.cursor()

    try : 
        for data in dataBagianFurnitur:
            namaBagianFurnitur = data["nama"]
            panjang = data["panjang"]
            lebar = data["lebar"]
            tinggi = data["tinggi"]

            idBagianFurnitur = execute_query(furniturService.insertBagianFurnitur, namaBagianFurnitur, panjang, lebar, tinggi, idFurnitur, cursor=cursor)

            for detailBagianFurnitur in data["detailBagianFurnitur"]:
                namaWarna = detailBagianFurnitur["warna"]
                idWarna = execute_query(warnaService.getWarnaByName, namaWarna, cursor=cursor)

                namaMaterial = detailBagianFurnitur["material"]
                idMaterial = execute_query(materialService.getMaterialByName, namaMaterial, cursor=cursor)

                harga = detailBagianFurnitur["harga"]
                stok = detailBagianFurnitur["stok"]

                execute_query(furniturService.insertDetailBagianFurnitur, idBagianFurnitur, idWarna, idMaterial, harga, stok)
        cursor.commit()
    except Exception as e :
        cursor.rollback()
        raise e
    finally :
        cursor.close()

def insertFurnitur(nama, deskripsi, dataBagianFurnitur):
    cursor = conn.cursor()
    try:

        idFurnitur = execute_query(furniturService.insertFurnitur, nama, deskripsi, cursor=cursor)

        for data in dataBagianFurnitur:
            namaBagianFurnitur = data["nama"]
            panjang = data["panjang"]
            lebar = data["lebar"]
            tinggi = data["tinggi"]

            idBagianFurnitur = execute_query(furniturService.insertBagianFurnitur, namaBagianFurnitur, panjang, lebar, tinggi, idFurnitur, cursor=cursor)

            for detailBagianFurnitur in data["detailBagianFurnitur"]:
                namaWarna = detailBagianFurnitur["warna"]
                idWarna = execute_query(warnaService.getWarnaByName, namaWarna, cursor=cursor)

                namaMaterial = detailBagianFurnitur["material"]
                idMaterial = execute_query(materialService.getMaterialByName, namaMaterial, cursor=cursor)

                harga = detailBagianFurnitur["harga"]
                stok = detailBagianFurnitur["stok"]

                execute_query(furniturService.insertDetailBagianFurnitur, idBagianFurnitur, idWarna, idMaterial, harga, stok)

        cursor.commit()
    except Exception as e:
        cursor.rollback()
        raise e
    finally :
        cursor.close()
    
