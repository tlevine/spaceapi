<html>
  <head>
    <style>
    table, tr, td { padding: 0; margin: 0; }
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
          <th colspan="72"></th>
        </tr>
      </thead>
      <tbody>
        % for week in weeks:
        <tr>
          <td class="date">{{week['date']}}</td>
          % for observation in week['observations']:
          <td class="{{observation['open']}}"><a href="{{observation['mirror_href']}}">X</a></td>
          % end
        </tr>
        % end
      </tbody>
      <tfoot>
        <tr>
          <td class="time">Time</td>
          % for hour in hours:
          <td colspan="12">{{hour}}</td>
          % end
        </tr>
      </tfoot>
    </table>
  </body>
</html>
