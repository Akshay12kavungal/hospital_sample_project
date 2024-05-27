
import django_tables2 as tables

from customer.models import Departments,Doctors




class DoctorsTable(tables.Table):
    class Meta:
        model = Doctors
        fields=("doc_name","doc_spec","dep_name","dep_image")
        table_title = "Doctors"
        edit_url = "update"
        detail_url = "detail"
        delete_url = "delete"



class DepartmentTable(tables.Table):
    actions = tables.TemplateColumn(
        verbose_name='Actions',
        template_code='''
        <a href="{% url "department_update" record.id %}" class="btn btn-warning btn-sm"> Edit</a> |
        <a href="{% url "department_detail" record.id %}" class="btn btn-info btn-sm">Detail</a> |
        <a href="{% url "department_delete" record.id %}" class="btn btn-danger btn-sm">Delete</a>
        '''
    )

    class Meta:
        model = Departments
        fields = ("dep_name", "dep_description", "actions")
        table_title = "Department"