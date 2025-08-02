from log_parser import load_logs, analyze, average_stats, sorted_average_stats, print_info, args_parser

def main():
    args = args_parser()
    logs = load_logs(args.file)
    analyze_logs = analyze(logs, date=args.date)
    avg_logs = average_stats(analyze_logs)
    avg_sorted_logs = sorted_average_stats(avg_logs)
    print_info(avg_sorted_logs)


if __name__ == '__main__':
    main()