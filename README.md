# device-selector

A small Python library to automatically pick the best available PyTorch device.
- `select_best_device()`
- `check_or_select_device(requested_device: Optional[str])`

Usage example:

```python
from device_selector import check_or_select_device
device = check_or_select_device()  # returns 'cuda', 'mps', or 'cpu'
...
