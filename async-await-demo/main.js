// import fs from 'fs';
// import path from 'path';
// import request from 'request';
//
// var movieDir = __dirname + '/movies',
//     exts     = ['.mkv', '.avi', '.mp4', '.rm', '.rmvb', '.wmv'];
//
// // 读取文件列表
// var readFiles = function () {
//     return new Promise(function (resolve, reject) {
//         fs.readdir(movieDir, function (err, files) {
//             resolve(files.filter((v) => exts.includes(path.parse(v).ext)));
//         });
//     });
// };
//
// // 获取海报
// var getPoster = function (movieName) {
//     let url = `https://api.douban.com/v2/movie/search?q=${encodeURI(movieName)}`;
//
//     return new Promise(function (resolve, reject) {
//         request({url: url, json: true}, function (error, response, body) {
//             if (error) return reject(error);
//
//             resolve(body.subjects[0].images.large);
//         })
//     });
// };
//
// // 保存海报
// var savePoster = function (movieName, url) {
//     request.get(url).pipe(fs.createWriteStream(path.join(movieDir, movieName + '.jpg')));
// };
//
//
// (async () => {
//     let files = await readFiles();
//
//     // await只能使用在原生语法
//     for (var file of files) {
//         let name = path.parse(file).name;
//
//         console.log(`正在获取【${name}】的海报`);
//         savePoster(name, await getPoster(name));
//     }
//
//     console.log('=== 获取海报完成 ===');
// })();

'use strict';

var _fs = require('fs');

var _fs2 = _interopRequireDefault(_fs);

var _path = require('path');

var _path2 = _interopRequireDefault(_path);

var _request = require('request');

var _request2 = _interopRequireDefault(_request);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { step("next", value); }, function (err) { step("throw", err); }); } } return step("next"); }); }; }

var movieDir = __dirname + '/movies',
    exts = ['.mkv', '.avi', '.mp4', '.rm', '.rmvb', '.wmv'];

// 读取文件列表
var readFiles = function readFiles() {
    return new Promise(function (resolve, reject) {
        _fs2.default.readdir(movieDir, function (err, files) {
            resolve(files.filter(function (v) {
                return exts.includes(_path2.default.parse(v).ext);
            }));
        });
    });
};

// 获取海报
var getPoster = function getPoster(movieName) {
    var url = 'https://api.douban.com/v2/movie/search?q=' + encodeURI(movieName);

    return new Promise(function (resolve, reject) {
        (0, _request2.default)({ url: url, json: true }, function (error, response, body) {
            if (error) return reject(error);

            resolve(body.subjects[0].images.large);
        });
    });
};

// 保存海报
var savePoster = function savePoster(movieName, url) {
    _request2.default.get(url).pipe(_fs2.default.createWriteStream(_path2.default.join(movieDir, movieName + '.jpg')));
};

_asyncToGenerator(regeneratorRuntime.mark(function _callee() {
    var files, _iteratorNormalCompletion, _didIteratorError, _iteratorError, _iterator, _step, file, name;

    return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
            switch (_context.prev = _context.next) {
                case 0:
                    _context.next = 2;
                    return readFiles();

                case 2:
                    files = _context.sent;


                    // await只能使用在原生语法
                    _iteratorNormalCompletion = true;
                    _didIteratorError = false;
                    _iteratorError = undefined;
                    _context.prev = 6;
                    _iterator = files[Symbol.iterator]();

                case 8:
                    if (_iteratorNormalCompletion = (_step = _iterator.next()).done) {
                        _context.next = 21;
                        break;
                    }

                    file = _step.value;
                    name = _path2.default.parse(file).name;


                    console.log('\u6B63\u5728\u83B7\u53D6\u3010' + name + '\u3011\u7684\u6D77\u62A5');
                    _context.t0 = savePoster;
                    _context.t1 = name;
                    _context.next = 16;
                    return getPoster(name);

                case 16:
                    _context.t2 = _context.sent;
                    (0, _context.t0)(_context.t1, _context.t2);

                case 18:
                    _iteratorNormalCompletion = true;
                    _context.next = 8;
                    break;

                case 21:
                    _context.next = 27;
                    break;

                case 23:
                    _context.prev = 23;
                    _context.t3 = _context['catch'](6);
                    _didIteratorError = true;
                    _iteratorError = _context.t3;

                case 27:
                    _context.prev = 27;
                    _context.prev = 28;

                    if (!_iteratorNormalCompletion && _iterator.return) {
                        _iterator.return();
                    }

                case 30:
                    _context.prev = 30;

                    if (!_didIteratorError) {
                        _context.next = 33;
                        break;
                    }

                    throw _iteratorError;

                case 33:
                    return _context.finish(30);

                case 34:
                    return _context.finish(27);

                case 35:

                    console.log('=== 获取海报完成 ===');

                case 36:
                case 'end':
                    return _context.stop();
            }
        }
    }, _callee, undefined, [[6, 23, 27, 35], [28,, 30, 34]]);
}))();