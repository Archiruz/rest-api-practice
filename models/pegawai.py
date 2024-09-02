# models/pegawai.py

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.sqltypes import Date

metadata = MetaData()
Pegawai = Table(
    "dt_pegawai", metadata,
    Column("id_pegawai", Integer, primary_key=True, index=True),
    Column("nama_pegawai", String(255), nullable=False),
    Column("alamat_pegawai", String(255)),
    Column("ttl_pegawai", Date()),
    Column("telp_pegawai", String(255)),
    Column("email_pegawai", String(255)),
)