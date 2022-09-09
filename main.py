from google.cloud.errorreporting_v1beta1.services.error_stats_service import ErrorStatsServiceClient
from google.cloud.errorreporting_v1beta1.services.error_group_service import ErrorGroupServiceClient
from google.cloud.errorreporting_v1beta1.types.error_group_service import GetGroupRequest
from google.cloud.errorreporting_v1beta1.types.error_stats_service import QueryTimeRange
from config import setting


def main():
    # use default credential
    client = ErrorStatsServiceClient()
    # get stats
    stats = client.list_group_stats(
        project_name=setting.project_name,
        time_range=QueryTimeRange(period=QueryTimeRange.Period.PERIOD_30_DAYS)
    )
    for item in stats:
        # print error stack trace
        print(item.representative.message)
        # print(item.group)
        
        # for stats in item.error_group_stats:
        #     print(stats)

    # get event
    # events = client.list_events(
    #     project_name=setting.project_name)
    # for p in events.pages:
    #     print(p.time_range_begin)
    #     print(p.error_events)

    # group_client = ErrorGroupServiceClient()
    # req = GetGroupRequest(
    #     group_name=f'{setting.project_name}/groups/*')
    # groups = group_client.get_group(req)
    # print(groups)


if __name__ == "__main__":
    main()
