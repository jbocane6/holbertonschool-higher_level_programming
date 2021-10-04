#include <stdio.h>
#include <strings.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
    PyListObject *list;
	long int i, list_size;
	PyObject *list_item;
	const char *list_item_type;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	list_size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		list_item = PyList_GET_ITEM(list, i);
		list_item_type = (list_item->ob_type)->tp_name;

		printf("Element %ld: %s\n", i, list_item_type);

		if (strcmp(list_item_type, "bytes") == 0)
			print_python_bytes(list_item);
		if (strcmp(list_item_type, "float") == 0)
			print_python_float(list_item);
	}
}
void print_python_bytes(PyObject *p)
{

}

void print_python_float(PyObject *p)
{

}