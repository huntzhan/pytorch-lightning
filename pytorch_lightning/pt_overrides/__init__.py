import warnings

warnings.warn("`pt_overrides` package has been renamed to `overrides` since v0.5.3"
              " and will be removed in v0.8.0", DeprecationWarning)

from pytorch_lightning.overrides import override_data_parallel  # noqa: E402
