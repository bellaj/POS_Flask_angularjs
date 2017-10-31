var QRCode = require('qrcode')
var canvas = document.getElementById('canvas')
 
QRCode.toCanvas(canvas, 'ethereum:0x7cB57B5A97eAbe94205C07890BE4c1aD31E486A8?value=2?gas=2100', function (error) {
  if (error) console.error(error)
  console.log('success!');
})
