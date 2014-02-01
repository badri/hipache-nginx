Removes all of the original hipache-nginx code. 

Bases the nginx reverse proxy Lua code on the code from the Paasmaker
routing component instead:

https://github.com/paasmaker/paasmaker/blob/master/paasmaker/router

However, it uses the hipache Redis storage scheme, which is simpler than
Paasmaker.

It should generally be functioning, though I stopped working on it when
I realized that I wouldn't be able to influence SNI negotiation via
Lua, and therefore cannot support multiple SSL vhosts:

https://github.com/chaoslawful/lua-nginx-module/issues/331
