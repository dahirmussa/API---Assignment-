var hprose = require("hprose");
var client = hprose.Client.create("//127.0.0.1:5000/");
var proxy = client.useService();
proxy.ping("world", function(result) {
    console.log(result);
});