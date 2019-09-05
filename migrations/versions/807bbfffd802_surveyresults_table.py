"""SurveyResults table

Revision ID: 807bbfffd802
Revises: 
Create Date: 2019-08-31 12:22:36.199943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '807bbfffd802'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('gender', sa.String(length=64), nullable=True),
    sa.Column('age', sa.String(length=20), nullable=True),
    sa.Column('recommendation', sa.String(length=20), nullable=True),
    sa.Column('like', sa.String(length=300), nullable=True),
    sa.Column('dislike', sa.String(length=300), nullable=True),
    sa.Column('organization', sa.String(length=20), nullable=True),
    sa.Column('helpful', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_survey_results_email'), 'survey_results', ['email'], unique=True)
    op.create_index(op.f('ix_survey_results_name'), 'survey_results', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_survey_results_name'), table_name='survey_results')
    op.drop_index(op.f('ix_survey_results_email'), table_name='survey_results')
    op.drop_table('survey_results')
    # ### end Alembic commands ###
