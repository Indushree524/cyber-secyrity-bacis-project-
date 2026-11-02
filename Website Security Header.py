
import requests

SECURITY_HEADERS = {
    "Strict-Transport-Security":
        "Protects against protocol downgrade attacks",

    "Content-Security-Policy":
        "Helps prevent Cross-Site Scripting (XSS)",

    "X-Content-Type-Options":
        "Prevents MIME type sniffing",

    "X-Frame-Options":
        "Helps prevent clickjacking attacks",

    "Referrer-Policy":
        "Controls referrer information",

    "Permissions-Policy":
        "Controls browser feature permissions"
}


def check_website(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print("\n================================")
    print(" WEBSITE SECURITY HEADER CHECKER")
    print("================================")

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "SecurityHeaderChecker/1.0"
            }
        )

        print("\nWebsite:", response.url)
        print("Status Code:", response.status_code)

        headers = response.headers

        print("\n--- SECURITY HEADER REPORT ---")

        secure_count = 0
        missing_count = 0

        for header, description in SECURITY_HEADERS.items():

            if header in headers:
                print("\n[FOUND]", header)
                print("Value:", headers[header])
                secure_count += 1

            else:
                print("\n[MISSING]", header)
                print("Purpose:", description)
                missing_count += 1

        print("\n================================")
        print("          FINAL REPORT")
        print("================================")

        print("Headers Found:", secure_count)
        print("Headers Missing:", missing_count)

        if missing_count == 0:
            print("Result: All checked headers are present.")

        elif secure_count >= 3:
            print("Result: Some security headers are missing.")

        else:
            print("Result: Several security headers are missing.")

        print("\nNote: Header presence does not guarantee")
        print("that the website is completely secure.")

    except requests.exceptions.SSLError:
        print("Error: SSL certificate verification failed.")

    except requests.exceptions.Timeout:
        print("Error: Website request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to website.")

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)


def main():

    print("================================")
    print("   WEBSITE SECURITY ANALYZER")
    print("================================")

    while True:

        website = input(
            "\nEnter website URL (or type exit): "
        ).strip()

        if website.lower() == "exit":
            print("Program closed.")
            break

        if not website:
            print("Please enter a valid website.")
            continue

        check_website(website)


if __name__ == "__main__":
    main()
