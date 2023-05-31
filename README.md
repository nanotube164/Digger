> ## Digger v1 feedback
> Digger is heading towards v2 and we would love to hear what _**you**_ would like to see in it. 
>
> **Thank you!**

![Digger](logo.png?raw=true)

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/spf13/viper/ci.yaml?branch=master&style=flat-square)](https://github.com/spf13/viper/actions?query=workflow%3ACI)
![Python Version]([https://img.shields.io/badge/go%20version-%3E=1.16-61CFDD.svg?style=flat-square](https://www.python.org/downloads/release/python-376/))


## Install

```shell
git clone git@github.com:nanotube164/Digger.git
```

## What is Digger?

Digger is a solution for collecting data from PI system including [22-Factor for MGGH](https://).
It is designed to organize data into an excel from PI system, and can handle 22 critical parameter for MGGH needs.
and formats. It supports:

* setting defaults
* reading from JSON, TOML, YAML, HCL, envfile and Java properties config files
* live watching and re-reading of config files (optional)
* reading from environment variables
* reading from remote config systems (etcd or Consul), and watching changes
* reading from command line flags
* reading from buffer
* setting explicit values

Digger can be thought of as a registry for all of your applications configuration needs.


## Why Digger?

When building a modern application, you don’t want to worry about
configuration file formats; you want to focus on building awesome software.
Viper is here to help with that.

Digger does the following for you:

1. Find, load, and unmarshal a configuration file in JSON, TOML, YAML, HCL, INI, envfile or Java properties formats.
2. Provide a mechanism to set default values for your different configuration options.
3. Provide a mechanism to set override values for options specified through command line flags.
4. Provide an alias system to easily rename parameters without breaking existing code.
5. Make it easy to tell the difference between when a user has provided a command line or config file which is the same as the default.

Digger uses the following precedence order. Each item takes precedence over the item below it:

 * explicit call to `Set`
 * flag
 * env
 * config
 * key/value store
 * default

**Important:** Viper configuration keys are case insensitive.
There are ongoing discussions about making that optional.


## Putting Values into Digger

### Establishing Defaults

A good configuration system will support default values. A default value is not
required for a key, but it’s useful in the event that a key hasn't been set via
config file, environment variable, remote configuration or flag.

Examples:

```go
viper.SetDefault("ContentDir", "content")
viper.SetDefault("LayoutDir", "layouts")
viper.SetDefault("Taxonomies", map[string]string{"tag": "tags", "category": "categories"})
```

## Q & A

### Why is it called “Digger”?

A: Digger is designed to be a [companion](http://en.wikipedia.org/wiki/Viper_(G.I._Joe))
to [Cobra](https://github.com/spf13/cobra). While both can operate completely
independently, together they make a powerful pair to handle much of your
application foundation needs.

### Why is it called “Cobra”?

Is there a better name for a [commander](http://en.wikipedia.org/wiki/Cobra_Commander)?

### Does Digger support case sensitive keys?

**tl;dr:** No.

Digger merges configuration from various sources, many of which are either case insensitive or uses different casing than the rest of the sources (eg. env vars).
In order to provide the best experience when using multiple sources, the decision has been made to make all keys case insensitive.

There has been several attempts to implement case sensitivity, but unfortunately it's not that trivial. We might take a stab at implementing it in [Viper v2](https://github.com/spf13/viper/issues/772), but despite the initial noise, it does not seem to be requested that much.

You can vote for case sensitivity by filling out this feedback form: https://forms.gle/R6faU74qPRPAzchZ9

### Is it safe to concurrently read and write to a viper?

No, you will need to synchronize access to the viper yourself (for example by using the `sync` package). Concurrent reads and writes can cause a panic.

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
