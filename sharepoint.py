import os
import tempfile

from office365.sharepoint.client_context import ClientContext


def download_file(ctx, file_url):
    download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
    with open(download_path, "wb") as local_file:
        file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
    print(f"[Ok] file {file_url} has been downloaded into: {download_path}")


if __name__ == "__main__":
    site_url = 'https://tturpin.sharepoint.com/sites/Turpin'

    cert_settings = {
        'tenant': 'd8176e28-***',
        'client_id': '413b47c5-***',
        'thumbprint': '76E9CD****',
        'cert_path': '/Users/thierryturpin/Library/Mobile Documents/com~apple~CloudDocs/Documents/Customer/TDP/selfsigncert.pem'
    }

    ctx = ClientContext(site_url).with_client_certificate(**cert_settings)

    file_url = 'Gedeelde documenten/General/PWC_LOGO.png'
    download_file(ctx, file_url)