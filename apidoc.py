"""
@api {post} /create/user Создание нового пользователя
@apiName Add User
@apiGroup Users

@apiParam {String} username Уникальное имя пользователя

@apiSuccess UserObject При удачном создании пользователя возвращается объект User в виде JSON.
@apiSuccessExample {json} Success-Response:
     {
        "userid": 1,
        "username": "name"
    }
@apiError UsernameError Указанное имя пользователя уже используется.
@apiError InvalidArguments Указаны не все аргументы.
"""