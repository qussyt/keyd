**Keyd**

> Keys parser for lololoshka shop

---

### Редактируете файл `config.json` в корневой директории с данным текстом:
```
{
  "vk_api_token": "<Ваш токен приложения, далее есть гайд его получения>",
  "default_screen_resolution": {
    "xver": <int значение вашего стандартного положения элемента "Соглашение" по оси x в px( Можно определить с помощью JustColorPicker )>,
    "yver": <int значение вашего стандартного положения элемента "Соглашение" по оси y в px( Можно определить с помощью JustColorPicker )>,
    "xsend": <int значение вашего стандартного положения элемента "Отправка" по оси x в px( Можно определить с помощью JustColorPicker )>,
    "xsend": <int значение вашего стандартного положения элемента "Отправка" по оси y в px( Можно определить с помощью JustColorPicker )>
  },
  "group_id": "lololoshkashop24"
}
```

---

### Как получить токен приложения:

1. Создаёте `Standalone-приложение` с любым названием [тут](https://vk.com/editapp?act=create).
2. Переходите к своему приложению.
3. Переходите в раздел `настройки`.
4. Копируете `Сервисный ключ доступа`.
5. Готово, это ваш токен приложения.

---

### Как определить координаты мыши:

1. [Скачиваете](https://annystudio.com/software/colorpicker/#download) и запускаете программу.
2. Переходите по [этой](https://store.steampowered.com/account/registerkey) ссылке и при необходимости авторизируетесь в стиме.
3. Открываете сначала `браузер` на весь экран, отодвигаете `JustColorPicker` в угол, где он не будет мешать, наводите мышь на необходимый элементы и записываете значения `x` и `y`, так-же и с другим элементом.
4. Готово, сохроняйте файл и пробуйте.

---

## Я не ручаюсь за работоспособность кода, т.к. на момент его написания он работал.
### Удачи 🎉

---

Версия Python: `3.9.1`
