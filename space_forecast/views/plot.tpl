<html>
  <head>
    <style>
    a.cell {
      display:inline-block;
      width: 8px;
      height: 16px;
    }
    a.cell, table, tr, td, th { padding: 0; margin: 0; border: 0; }
    #plot td { text-align: center; }
    #plot tbody td:nth-child(12n + 7) { padding-right: 3px; }
    #plot td.open a { background-color: black; }
    #plot td.closed a { background-color: grey; }
    #plot td.broken a { background-color: white; }
    </style>
  </head>
  <body>
    <h1>Is {{space}} open or closed? (Or is the space API broken?)</h1>
    <div id="plot">
      % for week in weeks:
      <div class="week">
        <span>{{week['date']}}</span>
        % for observation in week['observations']:
        <a class="cell {{observation['open']}}"
           title="{{observation['open']}}"
           href="{{observation['mirror_href']}}"></a>
        % end
      </div>
      % end


      </tbody>
      <tfoot>
        <tr>
          <th><a href="/{{space}}/{{earlier_day}}/{{earlier_hour}}">Earlier</a></th>
          % for hour in hours:
          <th colspan="12">{{hour}}</th>
          % end
          <th><a href="/{{space}}/{{later_day}}/{{later_hour}}">Later</a></th>
        </tr>
      </tfoot>
    </table>
  </body>
</html>
