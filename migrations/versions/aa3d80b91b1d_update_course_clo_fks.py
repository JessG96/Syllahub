"""update course clo fks

Revision ID: aa3d80b91b1d
Revises: 661647e76623
Create Date: 2019-04-12 16:11:19.464894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa3d80b91b1d'
down_revision = '661647e76623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(constraint_name='course_clo_ibfk_1', 
                       table_name='course_clo', 
                       type_='foreignkey')

    op.create_foreign_key(constraint_name='course_clo_ibfk_1',
                          source_table='course_clo', 
                          referent_table='clo', 
                          local_cols=['clo_id'], 
                          remote_cols=['id'], 
                          onupdate='CASCADE', 
                          ondelete='CASCADE')    


    op.drop_constraint(constraint_name='course_clo_ibfk_2', 
                       table_name='course_clo', 
                       type_='foreignkey')
    
    op.create_foreign_key(constraint_name='course_clo_ibfk_2',
                          source_table='course_clo', 
                          referent_table='course', 
                          local_cols=['course_number', 'course_version'], 
                          remote_cols=['number', 'version'], 
                          onupdate='CASCADE', 
                          ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(constraint_name='course_clo_ibfk_2', 
                       table_name='course_clo', 
                       type_='foreignkey')

    op.create_foreign_key(constraint_name='course_clo_ibfk_2',
                          source_table='course_clo', 
                          referent_table='course', 
                          local_cols=['course_number', 'course_version'], 
                          remote_cols=['number', 'version'])    


    op.drop_constraint(constraint_name='course_clo_ibfk_1', 
                       table_name='course_clo', 
                       type_='foreignkey')
    
    op.create_foreign_key(constraint_name='course_clo_ibfk_1',
                          source_table='course_clo', 
                          referent_table='clo', 
                          local_cols=['clo_id'], 
                          remote_cols=['id'])    
    # ### end Alembic commands ###
