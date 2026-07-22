# 🏗️ App Blueprint

## How does it work first?

1. You open the terminal
2. You run `just run`

then you see a beautiful asci art for the AI and then

```
Good Morning, [Name]! How can I help you today? ☺️

1. 💬 Let's chat 
2. ✅ Todo list
3. 📅 Calendar
4. 📝 Notes
5. ☁️ Backup
```

### Todo List

It opens todos db file: `~/.ai-partner/todos.db` and it helps you to work with it super easy

```
Here's your todos list:

1. Finish the meeting [🔥 DO FIRST]
2. Working out [📅 SCHEDULE]
3. Clean the car [🙅 DELEGATE]
4. Scroll Facebook [🗑️ DELETE]
```

Core features:

1. Add todo (with autocomplete when user typing to add it faster)
2. Edit/Remove todo
3. Sort todos by urgent
4. Move todos with `[🗑️ DELETE]` tag to the calendar app or delete them
5. Offer to move `[📅 SCHEDULE]` to the calendar
6. For `[🙅 DELEGATE]` offer to send a message politely to someone to do it for the user instead OR to drop it and say no
7. Offer to help him with `[🔥 DO FIRST]` using AI features
