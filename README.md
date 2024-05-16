
![Autobump ](https://github.com/Zectxr/disboard-autobump/blob/main/img.png)


# Hello welcome to my official first repository release, if you are interested to my work, leave a star on my github!



**Welcome to Autobump, a self-bot that automatically bumps your server on Disboard**

# Set-up

1. Download and extract the repository files.
2. Extract the `discord.py-self` master.zip.
3. Run `install.bat`.
4. Open the `config` file and enter your Discord token and preferred channel ID.
5. Finally, run `runner.bat`.

# How to get your token?

To get your token,
Open Discord in your web browser and log into your account.
Press Ctrl+Shift+I (or Cmd+Option+I on Mac) to open the Developer Tools.
Navigate to the Console tab in the Developer Tools.

Paste the following code into the console and press Enter:
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```






# WARNING

Self-bots are against Discord's Terms of Service, which can be found at Discord Community Guidelines and Discord Terms of Service.

This code is provided strictly for educational purposes.

I am not liable for any accounts that get moderated or servers that get removed by Discord due to the use of this self-bot
