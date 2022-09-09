import traceback
from google.cloud import errorreporting_v1beta1 as lib


def report_error():

    try:
        v = 100 / 0
    except:
        tracer = traceback.format_exc()
        send_error(tracer)


def send_error(tracer: str):
    client = lib.ReportErrorsServiceClient()
    event = lib.ReportedErrorEvent(
        message=tracer,
        # service_context=common.ServiceContext(service="My.Local.Application")
    )

    request = lib.ReportErrorEventRequest(
        project_name="projects/elite-monolith-334203",
        event=event,
    )
    client.report_error_event(
        request=request
    )


if __name__ == "__main__":
    report_error()
