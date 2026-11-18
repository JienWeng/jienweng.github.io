# Login — Mobile app

Everything a returning user needs to authenticate quickly and securely.

Source: https://www.checklist.design/mobile/login

## Items

### Social sign-in
Sign-in options that connect to an existing Apple or Google account, bypassing manual credential entry.

_Tip: On iOS, Apple Sign In is required by App Store guidelines if any other social provider is offered._

### Email field
The input where users enter the email address associated with their account.

### Password field
A masked text input for the account password, with the option to reveal what has been typed.

### Biometric authentication
Face ID or fingerprint sign-in for returning users who have already authenticated once with a password

_Tip: Encouraged to suggest after initial login so it’s a faster experience in the future_

### Credential autofill
System-level support for pre-filling saved email and password from the user's password manager.

_Tip: textContentType on iOS and autoComplete on Android are the attributes that trigger native autofill._

### Forgot password link
The link users reach for when they can't recall their password, leading into the reset flow.

### Error states
Feedback shown when authentication fails, distinguishing between an unrecognised email address and an incorrect password.

_Tip: Generic 'incorrect credentials' gives users no useful signal — knowing whether the email or password is wrong helps them recover without guessing._

### Passwordless sign-in (magic link)
An alternative sign-in method that sends a one-time link to the user's email, requiring no password

_Tip: Useful for infrequent-use apps where remembering a password between sessions is difficult_

## License for the Checklist Design collection

Checklist Design collection: https://github.com/Checklist-Design/skills
Snapshot: bfae71e507b1b7c03c12e0756402b60eb80f5d14 · Imported: 2026-11-12
Republished under the MIT License. Original checklist text belongs to Checklist Design.

MIT License

Copyright (c) 2026 Checklist Design

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
