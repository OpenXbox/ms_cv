# ms_cv - Correlation Vector

[![GitHub Workflow - Build](https://img.shields.io/github/workflow/status/OpenXbox/ms_cv/build?label=build)](https://github.com/OpenXbox/ms_cv/actions?query=workflow%3Abuild)
[![PyPi](https://img.shields.io/pypi/v/ms_cv.svg)](https://pypi.python.org/pypi/ms_cv)

A correlation vector implementation in python, based on Microsoft's implementation.

## Usage

```py
import ms_cv

cll_vec = ms_cv.CorrelationVector()
print('Initial cll vector: {}'.format(cll_vec.get_value()))
print('Next iteration: {}'.format(cll_vec.increment()))
```

## Installation

```sh
pip install ms_cv
```

## Requirements

* None

## Compatibility

* Python 3

## License

MIT LICENSE

## Authors

`ms_cv` was written by `OpenXbox <noreply@openxbox.org>`.

Based on the implementation by Microsoft:

<https://github.com/search?q=org%3Amicrosoft+correlationVector>

<https://github.com/Microsoft/Telemetry-Client-for-Android/blob/master/AndroidCll/src/main/java/com/microsoft/cll/android/CorrelationVector.java>
