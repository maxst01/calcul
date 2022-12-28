import model
import view
import logger

def start():
    model.set_first_number(view.input_number())
    operation = view.input_operation()

    while operation != '=':
        first = model.get_intermediate_result()
        model.set_next_number(view.input_number())
        second = model.get_next_number()
        oper = operation
        model.check_operation(operation)
        res = model.get_intermediate_result()
        view.print_result(model.get_intermediate_result())
        logger.logger(first, second, oper, res)
        operation = view.input_operation()

    view.print_result(model.get_intermediate_result())

