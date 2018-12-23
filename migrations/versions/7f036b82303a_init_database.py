"""init database

Revision ID: 7f036b82303a
Revises: 
Create Date: 2018-12-23 10:03:38.351252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f036b82303a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('website', sa.String(length=64), nullable=True),
    sa.Column('profile', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('website')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_table('jcity',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jcity_name'), 'jcity', ['name'], unique=True)
    op.create_table('jtag',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jtag_name'), 'jtag', ['name'], unique=True)
    op.create_table('salary_range',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('left', sa.Integer(), nullable=True),
    sa.Column('right', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('requirements', sa.String(length=1024), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('salary_range_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['salary_range_id'], ['salary_range.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_job_name'), 'job', ['name'], unique=True)
    op.create_table('job_city',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['jcity.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.PrimaryKeyConstraint('job_id', 'city_id')
    )
    op.create_table('job_tag',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['jtag.id'], ),
    sa.PrimaryKeyConstraint('job_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_tag')
    op.drop_table('job_city')
    op.drop_index(op.f('ix_job_name'), table_name='job')
    op.drop_table('job')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('salary_range')
    op.drop_index(op.f('ix_jtag_name'), table_name='jtag')
    op.drop_table('jtag')
    op.drop_index(op.f('ix_jcity_name'), table_name='jcity')
    op.drop_table('jcity')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
