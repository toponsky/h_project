'user strict';
const _ = require('lodash');

process.env.NODE_ENV = process.env.NODE_ENV || 'default';
const default_config = require('./config.json');
const defaultConfig = default_config.default;
const environment = process.env.NODE_ENV;
const environmentConfig = default_config[environment];
const finalConfig = _.merge(defaultConfig, environmentConfig);


config = finalConfig;
