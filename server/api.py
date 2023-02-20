from resources.user_api import Todo, TodoList

def init_api(api):
    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<todo_id>')