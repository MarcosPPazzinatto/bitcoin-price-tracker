from __future__ import annotations
try:
subprocess.run(shlex.split(args.on_alert), check=False)
except Exception as e:
print(f"warning: failed to run on-alert command: {e}", file=sys.stderr)


return 1 if fired else 0




def cmd_watch(args: argparse.Namespace) -> int:
n = 0
while args.times == 0 or n < args.times:
rc = cmd_price(args)
if n < args.times - 1 or args.times == 0:
time.sleep(args.interval)
n += 1
return rc




def cmd_chart(args: argparse.Namespace) -> int:
try:
series = get_market_chart(args.vs, days=args.days)
except ApiError as e:
print(f"error: {e}", file=sys.stderr)
return 2
prices = [p for _, p in series]
print(sparkline(prices))
return 0




def build_parser() -> argparse.ArgumentParser:
p = argparse.ArgumentParser(prog="btc-tracker", description="Minimal Bitcoin price tracker")
sub = p.add_subparsers(dest="cmd", required=True)


sp = sub.add_parser("price", help="Show current price")
sp.add_argument("--vs", default="USD", help="Fiat/crypto symbol, e.g., USD, BRL, EUR")
sp.add_argument("--alert-above", type=float, default=None)
sp.add_argument("--alert-below", type=float, default=None)
sp.add_argument("--on-alert", default=None, help="Command to run on alert (optional)")
sp.set_defaults(func=cmd_price)


sw = sub.add_parser("watch", help="Poll price repeatedly")
sw.add_argument("--vs", default="USD")
sw.add_argument("--interval", type=int, default=30, help="Seconds between pulls")
sw.add_argument("--times", type=int, default=0, help="How many pulls; 0 = infinite")
sw.add_argument("--alert-above", type=float, default=None)
sw.add_argument("--alert-below", type=float, default=None)
sw.add_argument("--on-alert", default=None)
sw.set_defaults(func=cmd_watch)


sc = sub.add_parser("chart", help="Print an ASCII sparkline for last N days (default 1)")
sc.add_argument("--vs", default="USD")
sc.add_argument("--days", type=int, default=1)
sc.set_defaults(func=cmd_chart)


return p




def main(argv: list[str] | None = None) -> int:
parser = build_parser()
args = parser.parse_args(argv)
return args.func(args)


if __name__ == "__main__":
raise SystemExit(main())
