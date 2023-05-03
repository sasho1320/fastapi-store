"""mirror many to many

Revision ID: a6547b63c303
Revises: 9342f946ee09
Create Date: 2023-05-03 15:54:29.596743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6547b63c303'
down_revision = '9342f946ee09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('books_reader_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'reader_id')
    op.drop_index('ix_readers_books_book_id', table_name='readers_books')
    op.drop_index('ix_readers_books_reader_id', table_name='readers_books')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_readers_books_reader_id', 'readers_books', ['reader_id'], unique=False)
    op.create_index('ix_readers_books_book_id', 'readers_books', ['book_id'], unique=False)
    op.add_column('books', sa.Column('reader_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('books_reader_id_fkey', 'books', 'readers', ['reader_id'], ['id'])
    # ### end Alembic commands ###
