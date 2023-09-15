from enum import Enum


class SinglesignonSSOProviderConfigSsoProviderType(str, Enum):
    GITHUB = "github"
    GOOGLE = "google"
    MICROSOFT = "microsoft"
    OIDC = "oidc"

    def __str__(self) -> str:
        return str(self.value)
