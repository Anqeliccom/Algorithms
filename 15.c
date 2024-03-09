#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    size_t capacity;
    size_t len;
} DynamicArr;

void create_dynamic_arr(DynamicArr* arr) {
    (*arr).capacity = 1;
    (*arr).data = (int*)malloc(sizeof(int) * (*arr).capacity);
    (*arr).len = 0;
}

void add_to_end(DynamicArr* arr, int elem) {
    if ((*arr).len == (*arr).capacity) {
        (*arr).capacity *= 2;
        (*arr).data = (int*)realloc((*arr).data, (*arr).capacity * sizeof(int));
    }
    (*arr).data[(*arr).len] = elem;
    (*arr).len++;
}

int get_by_index(DynamicArr* arr, size_t index) {
    return (*arr).data[index];
}

void delete_last(DynamicArr* arr) {
    if ((*arr).len < (*arr).capacity / 4) {
        (*arr).capacity /= 2;
        (*arr).data = (int*)realloc((*arr).data, (*arr).capacity * sizeof(int));
    }
    (*arr).len--;
}

void free_dynamic_arr(DynamicArr* arr) {
    free((*arr).data);
}

int main() {
    DynamicArr arr;
    create_dynamic_arr(&arr);

    int request;

    while (1) {
        printf("\nВыберите запрос:\n");
        printf("1) Добавить элемент в конец\n");
        printf("2) Получить элемент по индексу\n");
        printf("3) Удалить последний элемент\n");
        printf("4) Выйти\n");
        printf("Введите номер запроса: ");
        scanf("%d", &request);

        switch (request) {
            case 1: {
                int elem;
                printf("Введите значение: ");
                scanf("%d", &elem);
                add_to_end(&arr, elem);
                break;
            }
            case 2: {
                size_t index;
                printf("Введите индекс элемента: ");
                scanf("%lu", &index);
                if (index >= 0 && index < arr.len) {
                    printf("Элемент с индексом %lu: %d\n", index, get_by_index(&arr, index));
                } else {
                    printf("Индекс находится за пределами массива\n");
                }
                break;
            }
            case 3:
                if (arr.len == 0) {
                    printf("Массив пуст\n");
                } else {
                    delete_last(&arr);
                }
                break;
            case 4:
                free_dynamic_arr(&arr);
                return 0;
            default:
                printf("Некорректный номер запроса\n");
                break;
        }

        printf("Текущий массив: ");
        for (size_t i = 0; i < arr.len; i++) {
            printf("%d ", arr.data[i]);
        }
        printf("\n");
    }
}