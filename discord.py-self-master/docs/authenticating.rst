:orphan:

.. _authenticating:

Authenticating
==============

Tokens
-------

Tokens are how we authenticate with Discord. User accounts use the same token system as bots, received after authenticating with the Discord API.

How do I obtain mine?
----------------------
The library does not yet support authenticating traditionally, so you will have to obtain your token manually.

To obtain your token from the Discord client, the easiest way is pasting this into the developer console (CTRL+SHIFT+I):

.. code:: js

    (()=>{for(let e of Object.values(webpackChunkdiscord_app.push([[Symbol()],{},e=>e.c])))try{if(!e.exports||e.exports===window)continue;if(e.exports?.getToken)return e.exports.getToken();for(let t in e.exports)if(e.exports?.[t]?.getToken&&"IntlMessagesProxy"!==e.exports[t][Symbol.toStringTag])return e.exports[t].getToken()}catch{}})();


Or, you can do it manually:

1. Open developer tools (CTRL+SHIFT+I).
2. Click the Network tab.
3. Click the XHR tab.
4. Select a request and click the Headers tab.
5. Copy-paste the value in the Authorization header.
