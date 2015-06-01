<html>
  <head>
    <style>
    table { padding: 0; margin: 0; }
    #plot td { text-align: center; }
    #plot tbody td:nth-child(12n + 7) { border-right: solid 2px black; }
    #plot td.open { background-color: white; }
    #plot td.closed { background-color: black; }
    #plot td.broken { background-color: grey; }
    </style>
  </head>
  <body>
    <table id="plot">
      <thead>
        <tr>
          <th>Date</th>
          <th colspan="{{len(hours) * 12}}">Is {{space}} open or closed? (Or is the API broken?)</th>
        </tr>
      </thead>
      <tbody>
        % for week in weeks:
        <tr>
          <td class="date">{{week['date']}}</td>
          % for observation in week['observations']:
          <td class="{{observation['open']}}" title="{{observation['open']}}">
            <a href="{{observation['mirror_href']}}">X</a>
          </td>
          % end
        </tr>
        % end
      </tbody>
      <tfoot>
        <tr>
          <th class="time">Time</th>
          % for hour in hours:
          <th colspan="12">{{hour}}</th>
          % end
        </tr>
      </tfoot>
    </table>
  </body>
</html>
