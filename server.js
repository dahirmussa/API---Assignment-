var hprose = require("hprose");
function ping(name) {
    return "ping " + name + "!";
}
var server = hprose.Server.create("//127.0.0.1:5000/");
server.addFunction(ping);
server.start();