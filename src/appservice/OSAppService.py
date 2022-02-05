from ..repository.OSRepository import OSRepository

class OSAppService():
    def OS(func):
        try:
            OS = OSRepository.OS(func)
        except Exception as e:
            print(e)
        return {'data': OS, 'message': f'Success executing your function {func}'}