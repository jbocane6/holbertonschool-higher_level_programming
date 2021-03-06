#include <Python.h>
/**
* print_python_list_info - print python lists info
 * @p: list
*/
void print_python_list_info(PyObject *p)
{
    int tope = Py_SIZE(p), i = 0, cant = 0;
    PyObject *lista; 
    
    cant = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", tope, cant);
    for (; i <= tope - 1; i++)
    {
        lista = PyList_GetItem((p), (i));
        printf("Element %d: %s\n", i, Py_TYPE(lista)->tp_name);
    }
}
