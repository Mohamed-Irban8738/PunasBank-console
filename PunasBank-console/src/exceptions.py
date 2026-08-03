class AccountNotFoundError(Exception):
    """Raised when an account ID does not exist."""
    pass


class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when amount is zero or negative."""
    pass