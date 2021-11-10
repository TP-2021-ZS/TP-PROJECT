from WebProcessingUtils.WebProcessor import WebProcessor

processor = WebProcessor('./exports/', 'xlsx')

processor.process_url("https://akcie.sk/tesla-predbehla-facebook-a-prekonala-trhovu-hodnotu-1-biliona/")
