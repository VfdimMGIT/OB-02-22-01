# Класс для управления задачами
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")


# Класс для управления магазинами
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def __str__(self):
        return (f"Магазин: {self.name}\n"
                f"Адрес: {self.address}\n"
                f"Ассортимент: {self.items}")


# Основная программа
if __name__ == "__main__":
    # Демонстрация работы с задачами
    print("=== Демонстрация работы с задачами ===")
    task_manager = TaskManager()

    # Добавление задач
    task_manager.add_task("Купить молоко", "2025-01-22")
    task_manager.add_task("Позвонить другу", "2025-01-26")
    task_manager.add_task("Записаться на курс", "2025-01-27")

    # Отметка задачи как выполненной
    task_manager.mark_task_as_completed("Купить молоко")

    # Вывод текущих задач
    task_manager.show_current_tasks()
    print("\n")

    # Демонстрация работы с магазинами
    print("=== Демонстрация работы с магазинами ===")
    # Создаем три магазина
    store1 = Store("Фруктовый рай", "ул. Пушкина, 10")
    store2 = Store("Овощной дворик", "пр. Ленина, 25")
    store3 = Store("Молочная ферма", "ул. Гагарина, 7")

    # Добавляем товары в магазины
    store1.add_item("apples", 0.5)
    store1.add_item("bananas", 0.75)
    store1.add_item("oranges", 0.8)

    store2.add_item("potatoes", 0.3)
    store2.add_item("carrots", 0.4)
    store2.add_item("tomatoes", 0.9)

    store3.add_item("milk", 1.2)
    store3.add_item("cheese", 2.5)
    store3.add_item("yogurt", 1.0)

    # Выводим информацию о магазинах
    print("Информация о магазинах:")
    print(store1)
    print(store2)
    print(store3)
    print("\n")

    # Тестируем методы одного из магазинов (store1)
    print("=== Тестирование методов магазина 'Фруктовый рай' ===")
    store = store1

    # 1. Добавляем новый товар
    store.add_item("grapes", 1.2)
    print(store)

    # 2. Обновляем цену товара
    store.update_item_price("bananas", 0.9)
    print(store)

    # 3. Удаляем товар
    store.remove_item("oranges")
    print(store)

    # 4. Запрашиваем цену товара
    item_name = "apples"
    price = store.get_item_price(item_name)
    if price is not None:
        print(f"Цена товара '{item_name}': {price}")
    else:
        print(f"Товар '{item_name}' отсутствует в ассортименте.")

    # 5. Пробуем запросить цену несуществующего товара
    item_name = "pineapple"
    price = store.get_item_price(item_name)
    if price is not None:
        print(f"Цена товара '{item_name}': {price}")
    else:
        print(f"Товар '{item_name}' отсутствует в ассортименте.")