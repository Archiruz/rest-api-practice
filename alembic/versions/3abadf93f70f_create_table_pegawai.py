"""create table pegawai

Revision ID: 3abadf93f70f
Revises: 
Create Date: 2024-09-02 18:41:33.734437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from faker import Faker

faker = Faker('id_ID')

# revision identifiers, used by Alembic.
revision: str = '3abadf93f70f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pgw = op.create_table(
        'dt_pegawai',
        sa.Column('id_pegawai', sa.Integer, primary_key=True),
        sa.Column('nama_pegawai', sa.String(255), nullable=False),
        sa.Column('alamat_pegawai', sa.String(255)),
        sa.Column('ttl_pegawai', sa.Date()),
        sa.Column('telp_pegawai', sa.String(255)),
        sa.Column('email_pegawai', sa.String(255), unique=True)
    )
    op.bulk_insert(
        pgw,
        [{'nama_pegawai':faker.name(), 
                 'alamat_pegawai':faker.address(),
                 'ttl_pegawai':faker.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=28),
                 'telp_pegawai':faker.phone_number(),
                 'email_pegawai':faker.email()
                  } for x in range(100)]
    )


def downgrade():
    op.drop_table('dt_pegawai')