import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

MAILER_URL = "https://node-mailer-brown.vercel.app/send-email"
RECEIVER = "madarakatech@gmail.com"


# Create your views here.
def landing(request):
    return render(request, 'landing.html')


@csrf_exempt
@require_http_methods(["GET", "POST", "OPTIONS"])
def contact(request):
    if request.method == 'OPTIONS':
        return JsonResponse({}, status=200)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            company = data.get('company', '').strip()
            message = data.get('message', '').strip()

            if not name or not email or not message:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # ══ EMAIL 1 — Notify Madaraka ══
            admin_html = f"""
            <div style="font-family:sans-serif;max-width:600px;margin:auto;border:1px solid #eee;padding:32px;">
              <h2 style="color:#0a0a0a;border-bottom:2px solid #00F5FF;padding-bottom:12px;">
                📨 New Contact — Madaraka Technology
              </h2>
              <table style="width:100%;border-collapse:collapse;margin-top:16px;">
                <tr><td style="padding:8px 0;color:#666;width:120px;"><b>Name</b></td>
                    <td style="padding:8px 0;">{name}</td></tr>
                <tr><td style="padding:8px 0;color:#666;"><b>Email</b></td>
                    <td style="padding:8px 0;"><a href="mailto:{email}">{email}</a></td></tr>
                <tr><td style="padding:8px 0;color:#666;"><b>Company</b></td>
                    <td style="padding:8px 0;">{company or '—'}</td></tr>
                <tr><td style="padding:8px 0;color:#666;vertical-align:top;"><b>Message</b></td>
                    <td style="padding:8px 0;white-space:pre-wrap;">{message}</td></tr>
              </table>
              <p style="margin-top:24px;font-size:12px;color:#aaa;">Sent via madaraka.tech contact form</p>
            </div>
            """

            # ══ EMAIL 2 — Auto-reply to user ══
            user_html = f"""
            <div style="font-family:sans-serif;max-width:600px;margin:auto;background:#02030A;color:#E8EEFF;padding:40px;border-top:3px solid #00F5FF;">

              <!-- Logo bar -->
              <div style="display:flex;align-items:center;gap:12px;margin-bottom:32px;">
                <div style="width:36px;height:36px;border:1.5px solid #00F5FF;display:flex;align-items:center;justify-content:center;font-family:monospace;font-size:16px;color:#00F5FF;">▷</div>
                <div>
                  <div style="font-family:monospace;font-size:13px;letter-spacing:3px;color:#E8EEFF;">MADARAKA</div>
                  <div style="font-family:monospace;font-size:9px;letter-spacing:4px;color:#00F5FF;">TECHNOLOGY</div>
                </div>
              </div>

              <!-- Heading -->
              <h1 style="font-size:26px;font-weight:800;letter-spacing:2px;color:#00F5FF;margin:0 0 8px;">
                ENQUIRY RECEIVED
              </h1>
              <p style="font-size:13px;color:rgba(232,238,255,0.5);letter-spacing:1px;margin:0 0 28px;">
                TRANSMISSION CONFIRMED · REF #{abs(hash(email + name)) % 100000:05d}
              </p>

              <!-- Body -->
              <p style="font-size:15px;line-height:1.8;color:rgba(232,238,255,0.85);margin:0 0 16px;">
                Hi <strong style="color:#fff;">{name}</strong>,
              </p>
              <p style="font-size:15px;line-height:1.8;color:rgba(232,238,255,0.75);margin:0 0 16px;">
                Thank you for reaching out to <strong style="color:#00F5FF;">Madaraka Technology</strong>.
                We have successfully received your enquiry and our team will review it shortly.
              </p>
              <p style="font-size:15px;line-height:1.8;color:rgba(232,238,255,0.75);margin:0 0 32px;">
                You can expect to hear back from us <strong style="color:#fff;">within 24 hours</strong>.
                We look forward to exploring how we can build something great together.
              </p>

              <!-- Summary box -->
              <div style="border:1px solid rgba(0,245,255,0.2);padding:20px;margin-bottom:32px;background:rgba(0,245,255,0.04);">
                <div style="font-family:monospace;font-size:10px;letter-spacing:3px;color:#00F5FF;margin-bottom:12px;">// YOUR SUBMISSION</div>
                <table style="width:100%;border-collapse:collapse;font-size:13px;">
                  <tr>
                    <td style="padding:5px 0;color:rgba(232,238,255,0.4);width:90px;">Message</td>
                    <td style="padding:5px 0;color:rgba(232,238,255,0.8);font-style:italic;">"{message[:120]}{'...' if len(message) > 120 else ''}"</td>
                  </tr>
                </table>
              </div>

              <!-- No-reply notice -->
              <div style="border-left:2px solid rgba(0,245,255,0.3);padding:10px 16px;margin-bottom:32px;">
                <p style="font-family:monospace;font-size:11px;color:rgba(232,238,255,0.35);margin:0;line-height:1.7;">
                  ⚠ This is an automated message — please do not reply to this email.<br/>
                  To follow up, contact us directly at
                  <a href="mailto:{RECEIVER}" style="color:#00F5FF;text-decoration:none;">{RECEIVER}</a>
                </p>
              </div>

              <!-- Footer -->
              <div style="border-top:1px solid rgba(0,245,255,0.1);padding-top:20px;">
                <p style="font-family:monospace;font-size:10px;color:rgba(232,238,255,0.25);letter-spacing:2px;margin:0;">
                  © 2025 MADARAKA TECHNOLOGY — CS + TELECOM ENGINEERING — NAIROBI, KE
                </p>
              </div>

            </div>
            """

            # ── Send both emails ──
            admin_payload = {
                "name": "Madaraka Technology Website",
                "to": RECEIVER,
                "subject": f"New Enquiry from {name} — {company or 'No Company'}",
                "html_message": admin_html,
            }

            user_payload = {
                "name": "info@Madaraka Technologies",
                "to": email,
                "subject": "We've Received Your Enquiry — Madaraka Technologies",
                "html_message": user_html,
            }

            headers = {"Content-Type": "application/json"}

            admin_res = requests.post(MAILER_URL, json=admin_payload, headers=headers, timeout=10)
            user_res = requests.post(MAILER_URL, json=user_payload, headers=headers, timeout=10)

            if admin_res.status_code == 200:
                print(f"[CONTACT] ✓ Admin email sent — {name} <{email}>")
            else:
                print(f"[CONTACT] ✗ Admin email failed — {admin_res.status_code}: {admin_res.text}")

            if user_res.status_code == 200:
                print(f"[CONTACT] ✓ Auto-reply sent → {email}")
            else:
                print(f"[CONTACT] ✗ Auto-reply failed — {user_res.status_code}: {user_res.text}")

            # Return ok as long as admin email went through
            if admin_res.status_code == 200:
                return JsonResponse({'status': 'ok', 'message': 'Received'})
            else:
                return JsonResponse({'error': 'Email delivery failed'}, status=502)

        except requests.exceptions.Timeout:
            return JsonResponse({'error': 'Mailer service timed out'}, status=504)
        except Exception as e:
            print(f"[CONTACT] ✗ Exception — {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
