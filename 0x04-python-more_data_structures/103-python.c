
#include <Python.h>
/**
 * print_python_list - print list.
 * @p: pyobject.
 */
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p)
{
	unsigned long int tope = ((PyVarObject *)p)->ob_size, i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", tope);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < tope; i++)
		printf("Element %ld: %s\n", i, PySequence_GetItem(p, i)->ob_type->tp_name);
}
/**
 * print_python_bytes - print bytes.
 * @p: pyobject.
 */
void print_python_bytes(PyObject *p)
{
	(void)*p;
}